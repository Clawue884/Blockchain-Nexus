// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IToken {
    function mint(address to, uint256 amount) external;
    function burn(uint256 amount) external;
}
