# -*- coding: utf-8 -*-
"""
@author: Sandeepan
"""

def configurator(file_name='setup.cfg'):
    """
    Usage:
    SIGMA, BETA, RHO, ALPHA, GAMMA, DT, MSG_FILE = cfgr('setup.cfg')
    """

    configure = []
    configuration = open(file_name, 'r').readlines()
    for line in configuration:

        if "Sigma:" in line:
            sigma = str(line[:].split(":", 1)[1])
            sigma = sigma.replace('\n', '').replace('\0', '').replace(' ', '')
            sigma = float(sigma)
            configure.append(sigma)

        if "Beta:" in line:
            beta = str(line[:].split(":", 1)[1])
            beta = beta.replace('\n', '').replace('\0', '').replace(' ', '')
            beta = float(beta)
            configure.append(beta)

        if "Rho:" in line:
            rho = str(line[:].split(":", 1)[1])
            rho = rho.replace('\n', '').replace('\0', '').replace(' ', '')
            rho = float(rho)
            configure.append(rho)

        if "Gamma:" in line:
            gamma = str(line[:].split(":", 1)[1])
            gamma = gamma.replace('\n', '').replace('\0', '').replace(' ', '')
            gamma = float(gamma)
            configure.append(gamma)

        if "Alpha:" in line:
            alpha = str(line[:].split(":", 1)[1])
            alpha = alpha.replace('\n', '').replace('\0', '').replace(' ', '')
            alpha = float(alpha)
            configure.append(alpha)

        if "dt:" in line:
            dt = str(line[:].split(":", 1)[1])
            dt = dt.replace('\n', '').replace('\0', '').replace(' ', '')
            dt = float(dt)
            configure.append(dt)

        if "msg_file:" in line:
            msg_file = str(line[:].split(":", 1)[1])
            msg_file = msg_file.replace('\n', '').replace('\0', '').replace(' ', '')
            msg_file = str(msg_file)
            configure.append(msg_file)

    return configure


if __name__ == '__main__':
    configurator()
