import argparse
import json
from multiprocessing import Pool
from subprocess import call, Popen, PIPE


def parse_arguments():
    """Parse the runtime arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--suite', '-s', default='tests/features')
    parser.add_argument('--processes', '-p', type=int, default=5)
    parser.add_argument('--tags', '-t')
    return parser.parse_args()


def _run_parallel_feature(feature):
    """Runs the features passed to it"""
    cmd = 'behave -f allure_behave.formatter:AllureFormatter -o reports {feature}'.format(feature=feature)
    r = call(cmd, shell=True)

    status = 'Passed' if r == 0 else 'Failed'
    print('{0:50}: {1}!!'.format(feature, status))
    return feature, status


def main():
    """Run Behave in parallel"""
    args = parse_arguments()
    pool = Pool(args.processes)
    cmd = 'behave {suite}/. -t {tags} -d -f json --no-summary'.format(
        suite=args.suite, tags=args.tags)
    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()

    if err is not None:
        print(err)

    features = [scenario['location'] for scenario in json.loads(out.decode())]
    with open("features","w") as file:
        for feature in features:
            file.write("%s\n" % feature)

    pool.map(_run_parallel_feature, features)


if __name__ == '__main__':
    main()