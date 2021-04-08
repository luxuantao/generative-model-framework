import pathlib
import sys

abs_path = pathlib.Path(__file__).parent
sys.path.append('../model')

from predict import Predict
from data_utils import write_samples


def semi_supervised(samples_path, write_path, beam_search):
    """use reference to predict source

    Args:
        samples_path (str): The path of reference
        write_path (str): The path of new samples

    """
    pred = Predict()
    print('vocab_size: ', len(pred.vocab))
    # Randomly pick a sample in test set to predict.
    count = 0
    semi = []

    with open(samples_path, 'r') as f:
        for picked in f:
            count += 1
            source, ref = picked.strip().split('<sep>')
            prediction = pred.predict(ref.split(), beam_search=beam_search)
            semi.append(prediction + ' <sep> ' + ref)

            if count % 100 == 0:
                print(count)
                write_samples(semi, write_path, 'a')
                semi = []


if __name__ == '__main__':
    samples_path = '../files/train.txt'
    write_path_greedy = 'output/semi_greedy.txt'
    write_path_beam = 'output/semi_beam.txt'
    beam_search = False
    if beam_search:
        write_path = write_path_beam
    else:
        write_path = write_path_greedy
    semi_supervised(samples_path, write_path, beam_search)
