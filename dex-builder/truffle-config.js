// truffle-config.js
require('dotenv').config();
const HDWalletProvider = require('@truffle/hdwallet-provider');

const MNEMONIC = process.env.MNEMONIC;
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID;

module.exports = {
  // truffle-config.js
    networks: {
        development: {
            host: "127.0.0.1",
            port: 7545, // Ganache GUI port
            network_id: "*", // Match any network id
        },
        ropsten: {
            provider: () => new HDWalletProvider(MNEMONIC, `https://ropsten.infura.io/v3/${INFURA_PROJECT_ID}`),
            network_id: 3,       // Ropsten's id
            gas: 5500000,        // Ropsten has a lower block limit than mainnet
            confirmations: 2,     // # of confs to wait between deployments. (default: 0)
            timeoutBlocks: 200,   // # of blocks before a deployment times out  (minimum/default: 50)
            skipDryRun: true      // Skip dry run before migrations? (default: false for public nets )
        },
        mainnet: {
            provider: () => new HDWalletProvider(MNEMONIC, `https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`),
            network_id: 1,       // Mainnet's id
            gas: 5500000,        // Mainnet has a lower block limit than mainnet
            confirmations: 2,     // # of confs to wait between deployments. (default: 0)
            timeoutBlocks: 200,   // # of blocks before a deployment times out  (minimum/default: 50)
            skipDryRun: true      // Skip dry run before migrations? (default: false for public nets )
        }
    },
    compilers: {
        solc: {
            version: "0.8.0",    // Fetch exact version from solc-bin (default: truffle's version)
            settings: {          // See solc-js docs for advice about optimization and evmVersion
                optimizer: {
                    enabled: true,
                    runs: 200
                },
            }
        }
    }
};
