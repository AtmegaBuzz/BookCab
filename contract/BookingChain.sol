// SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

contract BookingChain{

    mapping(string => uint) central;
    address owner;
    string secretKey;

    constructor(){
        owner = msg.sender;
    }

    function setSecretKey(string memory _secretKey) public {
        require(owner==msg.sender,"Insufficient Permission");
        secretKey = _secretKey;
    }

    function pay(string memory bookingHash) public payable{
        central[bookingHash] = msg.value;
    }

    function getTotalBalance() public view returns(uint){
        require(owner==msg.sender,"Insufficient Permission");
        return address(this).balance;
    }

    function getBooking(string memory bookingHash) public view returns(uint){
        return central[bookingHash];
    }

    function transferFunds(string memory _secretkey,address transferTo) public{
        require(
            keccak256(bytes(secretKey))==keccak256(bytes(_secretkey)),
            "Invalid Key"
        );
        payable(transferTo).transfer(address(this).balance);
    }

}