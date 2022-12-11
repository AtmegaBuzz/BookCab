

const metamask = window.ethereum
const metaMaskErr = "Metamask is required for payments";


async function payBooking(bookingHash){
    console.log(bookingHash);
    try{
        await window.ethereum.request({ method:"eth_requestAccounts" });
    }
    catch{
        setError("Unable to connect to metamask");
    }
}

if (metamask === undefined){
    window.alert(metaMaskErr);
    $("#pay").css({'background-color':"grey"});
    $("#pay").click(()=>{
        window.alert(metaMaskErr);
    });
}

else{
}
