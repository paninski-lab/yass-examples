"""
Memory profiling (line by line) for the detection step

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run cluster_memory.py PATH_TO_CONFIG_FILE

Plot results:

mprof plot
"""
from pathlib import Path
import logging
import argparse
from datetime import datetime
from memory_profiler import profile
import yass
from yass import cluster


if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    start = datetime.now()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=str,
                        help="Path to config file")
    parser.add_argument("-l", "--logger", type=str,
                        help="YASS logger level",
                        default="WARNING")
    args = parser.parse_args()

    # configure logs from yass
    logging.getLogger("yass").setLevel(args.logger)
    # logs from this script
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(__name__)

    # set yass configuration parameters
    yass.set_config(args.config)

    CONFIG = yass.read_config()

    logger.info('Clustering started at second: %.2f',
                (datetime.now() - start).total_seconds())

    DIRECTORY = Path(CONFIG.data.root_folder, 'profiling')

    scores_clear = str(DIRECTORY / 'scores_clear.npy')
    spike_index_clear = str(DIRECTORY / 'spike_index_clear.npy')

    # detection
    profile(cluster.run)(scores_clear, spike_index_clear,
                         output_directory='profiling',
                         if_file_exists='overwrite',
                         save_results=True)

    logger.info('Clustering finished at second: %.2f',
                (datetime.now() - start).total_seconds())
