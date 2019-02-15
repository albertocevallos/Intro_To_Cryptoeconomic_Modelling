# Intro_To_Cryptoeconomic_Modelling

## Overview

This is the code for this Medium article published by Alberto Cevallos on using Python for mechanism design.

### Content

* Part I: Build a Simple Blockchain Using Python
* Part II: Design and Test Mechanism

Take into account that blockchain protocols couple different types of mechanisms for different purposes (using PoW or PoS for sybil control, or PBFT or Tendermint for decision making/consensus). Many combinations are possible but not all make sense.

Much of the design work consists in understanding what are the different attack vectors, governance objectives and desired  product requirements (eg. speed, level of security). From that point on, it's reverse engineering the desired outcome using cryptographic protocols and economic games (rewards, penalties, participation thresholds).

## Dependencies

* hashlib
* datetime

You can install the dependencies using [pip](https://pypi.org/project/pip/). 

## Usage

You can clone the jupyter notebook version [blockchain.ipynb](https://github.com/albertocevallos/Mechanism_Design_Using_Python/blob/master/blockchain.ipynb) file but I recommend using the Google colab link and run the code from [there](https://colab.research.google.com/drive/1U3Zp3SckhwussLox6Ko4lJCnUzl0lpE3).

## Credits

Thanks to [howcodeORG](https://github.com/howCodeORG/Simple-Python-Blockchain/blob/master/blockchain.py) for the base blockchain simulation code.
