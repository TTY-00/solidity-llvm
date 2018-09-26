pragma solidity ^0.4.24;

contract vartest{
    uint256 contractvar;
    uint256 contractvar1;
    uint256 contractvar2 = 5;
    

      function functointest(address paramvar1, uint256 paramvar2) public returns(uint256 returnvar) {
          uint256 functionvar1;
          uint256 functionvar2;
          uint256 functionvar3 = 5;
          
          contractvar2 = 7;
          contractvar = contractvar2 + contractvar1; 
          functionvar3 = functionvar2 + functionvar3;
      }
}
