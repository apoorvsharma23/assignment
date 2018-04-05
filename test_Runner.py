import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    featureFilePath = ' feature_files/message.feature '
    tagOptions = ''
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = tagOptions + featureFilePath +  commonRunnerOptions

    runner_with_options.main(fullRunnerOptions)
