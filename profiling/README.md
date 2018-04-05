# Profiling code

Note: Only compatible with Python 3.

Install requirements first:

```shell
pip install -r requirements.txt
```

## Memory

### Profiling the entire pipeline

This first script profiles every step in the pipeline

Docs:

```shell
python pipeline_memory.py --help
```

[See this for details](https://github.com/pythonprofilers/memory_profiler)


### Profiling single steps line by line

Docs for preprocess step:

```shell
mprof run preprocess_memory.py --help
```

Docs for detect step:

```shell
mprof run detect_memory.py --help
```


WIP

## CPU profiler

### Profiling the entire pipeline

Docs:

```shell
python pipeline_cpu.py --help
```

### Profiling single steps line by line

WIP