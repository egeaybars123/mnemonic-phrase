# mnemonic-phrase
This repository aims to generate mnemonic phrases based on BIP-39 word list.

The Python file will generate a 24-word mnemonic phrase based on a 256-bits entropy.
SHA-256 hash function is implemented for hashing the entropy and creating a checksum.

The BIP-39 word list is given in the repository. However, it can be found in the original
bitcoin github repository under the file bips (Bitcoin Improvement Proposal).
