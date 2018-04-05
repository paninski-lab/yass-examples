"""
Memory profiling for the pipeline, looks for a config.yaml file in the
same folder.

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run pipeline.py PATH_TO_CONFIG_FILE
"""
import logging
import argparse
from datetime import datetime
from memory_profiler import profile
import yass
from yass import preprocess, detect, cluster, templates, deconvolute


@profile
def main():
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

    logger.info('Preprocessing started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # preprocessing
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = preprocess.run()

    logger.info('Preprocessing finished and detection started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # detection
    (score, spike_index_clear,
     spike_index_all) = detect.run(standarized_path,
                                   standarized_params,
                                   channel_index,
                                   whiten_filter)

    logger.info('Detection finished and clustering started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # clustering
    spike_train_clear = cluster.run(score, spike_index_clear)

    logger.info('Clustering finished and templates started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # templates
    the_templates = templates.run(spike_train_clear)

    logger.info('templates finished and deconvolution started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # deconvolution
    deconvolute.run(spike_index_all, the_templates)

    logger.info('Deconvolution finished at second: %.2f',
                (datetime.now() - start).total_seconds())


if __name__ == '__main__':
    main()
