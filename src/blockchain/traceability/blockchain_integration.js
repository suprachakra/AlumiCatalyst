/*
Blockchain Integration Module
This script demonstrates how to interact with the Traceability smart contract using Web3.js.
*/

const Web3 = require('web3');
const contractABI = require('./TraceabilityABI.json'); // Assume ABI is exported to JSON
const contractAddress = '0xYourContractAddressHere'; // Replace with the deployed contract address

const web3 = new Web3('https://your-azure-ethereum-node.example.com');

const traceabilityContract = new web3.eth.Contract(contractABI, contractAddress);

async function recordEvent(sensorId, timestamp, details) {
  const accounts = await web3.eth.getAccounts();
  const receipt = await traceabilityContract.methods.recordEvent(sensorId, timestamp, details)
    .send({ from: accounts[0] });
  console.log('Event recorded:', receipt);
}

async function getEvent(eventId) {
  const event = await traceabilityContract.methods.getEvent(eventId).call();
  console.log('Event details:', event);
}

// Example usage:
(async () => {
  await recordEvent('sensor_001', Math.floor(Date.now() / 1000), "Sample production event");
  await getEvent(1);
})();
