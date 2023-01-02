
const metamask = window.ethereum
const metaMaskErr = "Metamask is required for payments";
let oneEthWei = 1000000000000000000n
let web3js = new Web3(metamask); 
let minimumEthTransfer = 0.01
let ContractABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "bookingHash",
				"type": "string"
			}
		],
		"name": "pay",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_secretKey",
				"type": "string"
			}
		],
		"name": "setSecretKey",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_secretkey",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "transferTo",
				"type": "address"
			}
		],
		"name": "transferFunds",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "bookingHash",
				"type": "string"
			}
		],
		"name": "getBooking",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getTotalBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
] 

const contractAddress = "0x8874E50bd62D1D7F46c8EFbBc767F17e5Bf5C3e9";
const contract = new web3js.eth.Contract(ContractABI,contractAddress);


async function getInrToWei(bookingCost){
    
    const resp = await fetch("https://api.coinbase.com/v2/exchange-rates?currency=ETH");
    const exchangeRates = await resp.json();
    return web3js.utils.toWei(((bookingCost / exchangeRates.data.rates.INR) + minimumEthTransfer).toString(),"ether");


}

async function payBooking(bookingHash,bookingCost){


    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    let bookingCostWei = await getInrToWei(bookingCost);

    let transactionParam = {
        from: accounts[0],
        value: "0x"+"100".toString(16),
        gas: "3000000".toString(16),
        gasPrice: "3000000".toString(16)
    }

    try{
        transaction = await contract.methods.pay(bookingHash).send(transactionParam);	
		success_booking_url = "http://"+window.location.host+`/booking-payment/${bookingHash}`
		console.log(success_booking_url)
		await fetch(success_booking_url);	
		location.reload(true);

    } catch{
        console.error("transaction failed");
    }
}

if (metamask === undefined){
    window.alert(metaMaskErr);
    $("#pay").css({'background-color':"grey"});
    $("#pay").click(()=>{
        window.alert(metaMaskErr);
    });
}

