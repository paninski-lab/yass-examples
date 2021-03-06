import logging
from datetime import datetime
from memory_profiler import profile
from yass import preprocess, detect, cluster, templates, deconvolute
import settings


@profile
def main():
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    logger.info('Preprocessing started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # preprocessing
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = preprocess.run(output_directory='profiling',
                                     if_file_exists='overwrite')

    logger.info('Preprocessing finished and detection started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # detection
    (score, spike_index_clear,
     spike_index_all) = detect.run(standarized_path,
                                   standarized_params,
                                   channel_index,
                                   whiten_filter,
                                   output_directory='profiling',
                                   if_file_exists='overwrite',
                                   save_results=True)

    logger.info('Detection finished and clustering started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # clustering
    spike_train_clear = cluster.run(score, spike_index_clear,
                                    output_directory='profiling',
                                    if_file_exists='overwrite',
                                    save_results=True)

    logger.info('Clustering finished and templates started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # templates
    the_templates = templates.run(spike_train_clear,
                                  output_directory='profiling',
                                  if_file_exists='overwrite',
                                  save_results=True)

    logger.info('templates finished and deconvolution started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # deconvolution
    deconvolute.run(spike_index_all, the_templates,
                    output_directory='profiling')

    logger.info('Deconvolution finished at second: %.2f',
                (datetime.now() - start).total_seconds())


if __name__ == '__main__':
    main()
