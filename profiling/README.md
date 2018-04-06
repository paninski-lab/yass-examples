# Profiling code

Note: Only compatible with Python 3.

Install requirements first:

```shell
pip install -r requirements.txt
```

## Generating results from all steps

To be able to run steps separately, all the results from previous steps
need to be generated, run the following script to do so:

```shell
python memory_pipeline.py PATH_TO_CONFIG --logger INFO
```

Note: this won't do memory profiling, it is just to generate the files.

All results will be saved on `CONFIG.data.root_folder/profiling/`

## Memory

Run with:

```
mprof run memory_STEP.py PATH_TO_CONFIG
```

Where STEP is `preprocess`, `detect`, `cluster`, `templates`, `decovolution`
(profile one step in the pipeline line by line). `pipeline` is also valid, it runs the complete pipeline.

Run any of the scripts with the `--help` option to see more details.

Plot results:

```
mprof plot
```

## CPU

Run with:

```shell
kernprof -l cpu_STEP.py PATH_TO_CONFIG
```

Inspect results:

```shell
python -m line_profiler cpu_STEP.py.lprof
```


## Profiling everything

There is a script to profile eveything (takes a while to run):

```
./profile PATH_TO_CONFIG PATH_TO_OUTPUT > profile.log
```

This will generate `*.dat` (results from memory profiling), `*.png` (plots from memory profiling),  `.lprof` (results from cpu profiling), `.txt`
(cpu results in txt format) and a `profile.log` file in the `PATH_TO_OUTPUT`.

## Resources

* [Memory profiling library](https://github.com/pythonprofilers/memory_profiler)
* [CPU profiling library](https://github.com/rkern/line_profiler)

