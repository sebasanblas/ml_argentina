#!/usr/bin/env python3

'''
Módulo para instalar dependencias necesarias para el script

Ver 'requirements.txt' para las dependencias a instalar
'''

import pip

pip.main(['install', '--user', '-r', '../requirements.txt'])
