
======= vartest.sol:vartest =======
EVM assembly:
    /* "vartest.sol":26:489  contract vartest{... */
  mstore(0x40, 0x80)
    /* "vartest.sol":122:123  5 */
  0x5
    /* "vartest.sol":99:123  uint256 contractvar2 = 5 */
  0x2
  sstore
    /* "vartest.sol":26:489  contract vartest{... */
  callvalue
    /* "--CODEGEN--":8:17   */
  dup1
    /* "--CODEGEN--":5:7   */
  iszero
  tag_1
  jumpi
    /* "--CODEGEN--":30:31   */
  0x0
    /* "--CODEGEN--":27:28   */
  dup1
    /* "--CODEGEN--":20:32   */
  revert
    /* "--CODEGEN--":5:7   */
tag_1:
    /* "vartest.sol":26:489  contract vartest{... */
  pop
  dataSize(sub_0)
  dup1
  dataOffset(sub_0)
  0x0
  codecopy
  0x0
  return
stop

sub_0: assembly {
        /* "vartest.sol":26:489  contract vartest{... */
      mstore(0x40, 0x80)
      jumpi(tag_1, lt(calldatasize, 0x4))
      calldataload(0x0)
      0x100000000000000000000000000000000000000000000000000000000
      swap1
      div
      0xffffffff
      and
      dup1
      0x95f9f02e
      eq
      tag_2
      jumpi
    tag_1:
      0x0
      dup1
      revert
        /* "vartest.sol":137:487  function functointest(address paramvar1, uint256 paramvar2) public returns(uint256 returnvar) {... */
    tag_2:
      callvalue
        /* "--CODEGEN--":8:17   */
      dup1
        /* "--CODEGEN--":5:7   */
      iszero
      tag_3
      jumpi
        /* "--CODEGEN--":30:31   */
      0x0
        /* "--CODEGEN--":27:28   */
      dup1
        /* "--CODEGEN--":20:32   */
      revert
        /* "--CODEGEN--":5:7   */
    tag_3:
        /* "vartest.sol":137:487  function functointest(address paramvar1, uint256 paramvar2) public returns(uint256 returnvar) {... */
      pop
      tag_4
      0x4
      dup1
      calldatasize
      sub
      dup2
      add
      swap1
      dup1
      dup1
      calldataload
      0xffffffffffffffffffffffffffffffffffffffff
      and
      swap1
      0x20
      add
      swap1
      swap3
      swap2
      swap1
      dup1
      calldataload
      swap1
      0x20
      add
      swap1
      swap3
      swap2
      swap1
      pop
      pop
      pop
      jump(tag_5)
    tag_4:
      mload(0x40)
      dup1
      dup3
      dup2
      mstore
      0x20
      add
      swap2
      pop
      pop
      mload(0x40)
      dup1
      swap2
      sub
      swap1
      return
    tag_5:
        /* "vartest.sol":212:229  uint256 returnvar */
      0x0
        /* "vartest.sol":243:263  uint256 functionvar1 */
      dup1
        /* "vartest.sol":275:295  uint256 functionvar2 */
      0x0
        /* "vartest.sol":307:327  uint256 functionvar3 */
      dup1
        /* "vartest.sol":330:331  5 */
      0x5
        /* "vartest.sol":307:331  uint256 functionvar3 = 5 */
      swap1
      pop
        /* "vartest.sol":369:370  7 */
      0x7
        /* "vartest.sol":354:366  contractvar2 */
      0x2
        /* "vartest.sol":354:370  contractvar2 = 7 */
      dup2
      swap1
      sstore
      pop
        /* "vartest.sol":411:423  contractvar1 */
      sload(0x1)
        /* "vartest.sol":396:408  contractvar2 */
      sload(0x2)
        /* "vartest.sol":396:423  contractvar2 + contractvar1 */
      add
        /* "vartest.sol":382:393  contractvar */
      0x0
        /* "vartest.sol":382:423  contractvar = contractvar2 + contractvar1 */
      dup2
      swap1
      sstore
      pop
        /* "vartest.sol":466:478  functionvar3 */
      dup1
        /* "vartest.sol":451:463  functionvar2 */
      dup3
        /* "vartest.sol":451:478  functionvar2 + functionvar3 */
      add
        /* "vartest.sol":436:478  functionvar3 = functionvar2 + functionvar3 */
      swap1
      pop
        /* "vartest.sol":137:487  function functointest(address paramvar1, uint256 paramvar2) public returns(uint256 returnvar) {... */
      pop
      pop
      pop
      swap3
      swap2
      pop
      pop
      jump	// out

    auxdata: 0xa165627a7a723058207d9d29e77f0598608cb509d228b01c6e7356f2b8e4103a7d1f8b083408ef93bb0029
}

