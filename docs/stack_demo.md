# How to run Demo version of Scarlet

## Stack Version

Development on this sprint landed on the `deblender_sprint` branch. The demo output was run using the `w_2019_19` shared stack on lsst-dev + 5 local repos:

```[yusra@lsst-dev01]$ eups list -s | grep LOCAL
autograd              LOCAL:/project/yusra/lsst_devel/autograd/_eupspkg/binary/autograd/master-g6a9ef8c4bf      setup
meas_extensions_scarlet LOCAL:/project/yusra/lsst_devel/meas_extensions_scarlet         setup
pipe_drivers          LOCAL:/project/yusra/lsst_devel/pipe_drivers      setup
pipe_tasks            LOCAL:/project/yusra/lsst_devel/pipe_tasks        setup
scarlet               LOCAL:/project/yusra/lsst_devel/scarlet/_eupspkg/binary/scarlet/deblender_sprint-gc57351e96f      setup
```

To setup a demo stack:

```bash
 source /software/lsstsw/stack/loadLSST.bash 
 source scl_source enable devtoolset-6
 source scl_source enable rh-git29
 setup lsst_distrib -t w_2019_19
 
 git clone https://github.com/lsst-dm/autograd
 cd autograd
 # rm -r _eupspkg if you need to rebuild
 eupspkg -e -v 1 fetch
 eupspkg -e -v 1 prep
 eupspkg -e -v 1 config
 eupspkg -e -v 1 build
 eupspkg -e -v 1 install
 
  cd ..
  git clone https://github.com/lsst/scarlet
  cd scarlet
  git checkout deblender_sprint
  # rm -r _eupspkg if you need to rebuild
  eupspkg -e -v 1 fetch
  eupspkg -e -v 1 prep
  eupspkg -e -v 1 config
  eupspkg -e -v 1 build
  eupspkg -e -v 1 install
 
  cd ..
  git clone https://github.com/lsst/meas_extensions_scarlet
  git checkout deblender_sprint
  scons -j 4
  # flake 8 will complain. Ignore for now. 
  
  cd ..
  git clone https://github.com/lsst/pipe_tasks
  cd pipe_tasks
  git checkout deblender_sprint
  scons -j 4
  
  # Need master of pipe_drivers
  cd ..
  git clone https://github.com/lsst/pipe_drivers 
  cd pipe_drivers
  scons -j 4  
```

## Running Data

### CommandlineTask

You've already run `mergeCoaddDetections.py`

```
deblendCoaddSources.py  /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/yusra/deblender-sprint/scratch/initial_test_05k -c simultaneous=True multiBandDeblend.symmetric=False multiBandDeblend.catchFailures=True --id tract=9813 patch=18,25 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --no-versions
```

and now you're ready to run `measureCoaddSources.py`

### MultiBandDriver

Patch lists:

```bash
export TINY0=15,8^15,9^15,10^15,11^15,12^15,13^15,14^15,15^15,16^15,17^15,18^15,19^15,20^15,21^15,22^15,23^15,24^15,25^15,26^15,27^15,28^15,29^15,30^15,31^16,8^16,9^16,10^16,11^16,12^16,13^16,14^16,15^16,16^16,17^16,18^16,19^16,20^16,21^16,22^16,23^16,24^16,25^16,26^16,27^16,28^16,29^16,30^16,31^17,8^17,9^17,10^17,11^17,12^17,13^17,14^17,15^17,16^17,17^17,18^17,19^17,20^17,21^17,22^17,23^17,24^17,25^17,26^17,27^17,29^17,30^17,31^18,8^18,9^18,10^18,11^18,12^18,13^18,14^18,15^18,16
export TINY1=18,17^18,18^18,19^18,20^18,21^18,22^18,23^18,24^18,25^18,26^18,27^18,28^18,29^18,30^18,31^19,8^19,9^19,10^19,11^19,12^19,13^19,14^19,15^19,16^19,17^19,18^19,19^19,20^19,21^19,22^19,23^19,24^19,25^19,26^19,27^19,28^19,29^19,30^19,31^20,8^20,9^20,10^20,11^20,12^20,13^20,14^20,15^20,16^20,17^20,18^20,19^20,20^20,21^20,22^20,23^20,24^20,25^20,26^20,27^20,28^20,29^20,30^20,31^21,8^21,9^21,10^21,11^21,12^21,13^21,14^21,15^21,16^21,17^21,18^21,19^21,20^21,21^21,22^21,23^21,24^21,25
export TINY2=21,26^21,27^21,28^21,29^21,30^21,31^22,8^22,9^22,10^22,11^22,12^22,13^22,14^22,15^22,16^22,17^22,18^22,19^22,20^22,21^22,22^22,23^22,24^22,25^22,26^22,27^22,28^22,29^22,30^22,31^23,8^23,9^23,10^23,11^23,12^23,13^23,14^23,15^23,16^23,17^23,18^23,19^23,20^23,21^23,22^23,23^23,24^23,25^23,26^23,27^23,28^23,29^23,30^23,31^24,8^24,9^24,10^24,11^24,12^24,13^24,14^24,15^24,16^24,17^24,18^24,19^24,20^24,21^24,22^24,23^24,24^24,25^24,26^24,27^24,28^24,29^24,30^24,31^25,8^25,9^25,10
export TINY3=25,11^25,12^25,13^25,14^25,15^25,16^25,17^25,18^25,19^25,20^25,21^25,22^25,23^25,24^25,25^25,26^25,27^25,28^25,29^25,30^25,31^26,8^26,9^26,10^26,11^26,12^26,13^26,14^26,15^26,16^26,17^26,18^26,19^26,20^26,21^26,22^26,23^26,24^26,25^26,26^26,27^26,28^26,29^26,30^26,31^27,8^27,9^27,10^27,11^27,12^27,13^27,14^27,15^27,16^27,17^27,18^27,19^27,20^27,21^27,22^27,23^27,24^27,25^27,26^27,27^27,28^27,29^27,30^27,31^28,8^28,9^28,10^28,11^28,12^28,13^28,14^28,15^28,16^28,17^28,18^28,19
export TINY4=28,20^28,21^28,22^28,23^28,24^28,25^28,26^28,27^28,28^28,29^28,30^28,31^29,8^29,9^29,10^29,11^29,12^29,13^29,14^29,15^29,16^29,17^29,18^29,19^29,20^29,21^29,22^29,23^29,24^29,25^29,26^29,27^29,28^29,29^29,30^29,31^30,8^30,9^30,10^30,11^30,12^30,13^30,14^30,15^30,16^30,17^30,18^30,19^30,20^30,21^30,22^30,23^30,24^30,25^30,26^30,27^30,28^30,29^30,30^30,31^31,8^31,9^31,10^31,11^31,12^31,13^31,14^31,15^31,16^31,17^31,18^31,19^31,20^31,21^31,22^31,23^31,24^31,25^31,26^31,27^31,28

Need to run patch 17,28 on its own. 
```
Run like:

Note my `yusra` in the output repo was replaced with `username` so that you don't accidentally clobber if you copy and paste. 

```bash
multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY0 --nodes 6 --procs 2 --time 10000 --id tract=9813 patch=$TINY0 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False

multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY1 --nodes 6 --procs 2 --time 10000 --id tract=9813 patch=$TINY1 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False

multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY2 --nodes 6 --procs 2 --time 10000 --id tract=9813 patch=$TINY2 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False

multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY3 --nodes 6 --procs 2 --time 10000 --id tract=9813 patch=$TINY3 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False

multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY4 --nodes 6 --procs 2 --time 10000 --id tract=9813 patch=$TINY4 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False 

# patch=17,28 gets its own node
multiBandDriver.py /datasets/hsc/repo --calib /datasets/hsc/repo/CALIB/ --rerun private/yusra/deblender-sprint/w_2019_18_05k:private/username/deblender-sprint/scarlet/w_2019_18_05k_noSym_demo --batch-type=slurm --mpiexec='-bind-to socket' --job TINY4 --nodes 1 --procs 1 --time 10000 --id tract=9813 patch=17,28 filter=HSC-G^HSC-R^HSC-I^HSC-Z^HSC-Y^NB0921 --config deblendCoaddSources.simultaneous=True  deblendCoaddSources.multiBandDeblend.catchFailures=True measureCoaddSources.inputCatalog=deblendedModel deblendCoaddSources.multiBandDeblend.symmetric=False 
```

If you need to restart any use `--reuse-outputs-from all`
