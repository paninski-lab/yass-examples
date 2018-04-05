"""
CPU profiling using line_profiler

To run:

kernprof -l cpu.py yass.preprocess.run


Inspect results:


python -m line_profiler cpu.py.lprof

Docs:

https://github.com/rkern/line_profiler
"""
from pydoc import locate
import argparse
import logging
import yass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function", type=str,
                        help="Path to function to profile")
    parser.add_argument("-l", "--logger", type=str, help="Logger level",
                        default="INFO")
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.logger))
    yass.set_config('config.yaml')

    function = locate(args.function)

    to_profile = profile(function)
    to_profile(if_file_exists='overwrite')
