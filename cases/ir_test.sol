pragma solidity ^0.4.24;

contract ERC721Basic {

    function balanceOf(uint256 a, uint256 b) public view returns (uint256 _balance){
        return a + b;
    }
}
