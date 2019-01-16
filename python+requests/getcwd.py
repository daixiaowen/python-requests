import os


def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    # 当前文件的绝对路径
    return path


def get_casePath(caseDir, caseName=None):
    casePath = os.path.join(os.getcwd(), caseDir) + caseName
    return casePath


def get_report(reportDir, reportName=None):
    reportPath = os.path.join(get_cwd(), reportDir) + reportName
    return reportPath
