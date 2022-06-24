// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Ankit0Token is ERC20 {
    constructor(uint256 initialSupply) ERC20("Ankit0Token", "ANKIT0") {
        _mint(msg.sender, initialSupply);
    }
}