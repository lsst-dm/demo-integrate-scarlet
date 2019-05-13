import numpy as np
from lsst.daf.persistence import Butler
from lsst.geom import Box2I, Box2D, Point2I, Point2D, Extent2I, Extent2D
from lsst.afw.image import Exposure, Image, PARENT, MultibandExposure, MultibandImage
from lsst.afw.detection import MultibandFootprint

import lsst.meas.extensions.scarlet as scarlet

butler = Butler("/datasets/hsc/repo/rerun/RC/w_2019_14/DM-18300")
dataId = {"tract": 9813, "patch": "4,4"}
filters = "grizy"
coadds = [butler.get("deepCoadd_calexp", dataId, filter="HSC-{}".format(f.upper())) for f in filters]
coadds = MultibandExposure.fromExposures(filters, coadds)


from lsst.meas.algorithms import SourceDetectionTask
from lsst.meas.extensions.scarlet import ScarletDeblendTask
from lsst.meas.base import SingleFrameMeasurementTask
from lsst.afw.table import SourceCatalog

schema = SourceCatalog.Table.makeMinimalSchema()

detectionTask = SourceDetectionTask(schema=schema)

config = ScarletDeblendTask.ConfigClass()
config.maxIter = 100
deblendTask = ScarletDeblendTask(schema=schema, config=config)

# We'll customize the configuration of measurement to just run a few plugins.
# The default list of plugins is much longer (and hence slower).
measureConfig = SingleFrameMeasurementTask.ConfigClass()
measureConfig.plugins.names = ["base_SdssCentroid", "base_PsfFlux", "base_SkyCoord"]
# "Slots" are aliases that provide easy access to certain plugins.
# Because we're not running the plugin these slots refer to by default,
# we need to disable them in the configuration.
measureConfig.slots.apFlux = None
#measureConfig.slots.instFlux = None
measureConfig.slots.shape = None
measureConfig.slots.modelFlux = None
measureConfig.slots.calibFlux = None
measureConfig.slots.gaussianFlux = None
measureTask = SingleFrameMeasurementTask(config=measureConfig, schema=schema)



frame = 50
sampleBBox = Box2I(Point2I(19141-frame, 18228-frame), Extent2I(63+2*frame, 87+2*frame))
subset = coadds[:, sampleBBox]
# Due to a bug in the code the PSF isn't copied properly.
# The code below copies the PSF into the `MultibandExposure`,
# but will be unecessary in the future
for f in subset.filters:
    subset[f].setPsf(coadds[f].getPsf())
table = SourceCatalog.Table.make(schema)
detectionResult = detectionTask.run(table, subset["r"])
catalog = detectionResult.sources




idx = 0
for k, src in enumerate(catalog):
    if len(src.getFootprint().peaks) > len(catalog[idx].getFootprint().peaks):
        idx = k
footprint = catalog[idx].getFootprint()
bbox = footprint.getBBox()
mExposure = coadds[:, bbox]

import cProfile
cProfile.run("deblendTask.run(coadds, catalog[idx:idx+1])", 'callstack_profile.cprof')

result = deblendTask.run(coadds, catalog[idx:idx+1])




import lsst.afw.table as afwTable

for f in filters:
    _catalog = afwTable.SourceCatalog(result[1][f].table.clone())
    _catalog.extend(result[1][f], deep=True)
    result[1][f] = _catalog

print(result[1]["g"]["runtime"])
print(result[1]["g"]["iterations"])
