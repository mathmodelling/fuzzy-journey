# RANDOMNESS ANALYSIS

  ## My own script version of the Runs Test
  
  This version is based on the descriptions of the Runs Test presented in<span id="a1">[¹](#1)</span>


  The Excel data to be read uses the following template:
  
  | Año |Col1|Col2|...|ColN|
  | --- |--- |--- |---|--- |
  | XXXX|XXXX|XXXX|...|XXXX|
  | XXXX|XXXX|XXXX|...|XXXX|
  | ... | ...| ...|...|... |
  | XXXX|XXXX|XXXX|...|XXXX|
  
  Column titles should start at the first row and first column. Usually, Col1, Col2, and Coln interpret as months, but any other interpretation is also allowed. The Excel file can contain several sheets; the script will proceed with the randomness test over each sheet's columns.
  
  ## Using the RandomSuite
  
  The Python Random Suite is is a Python implementation of NIST's Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications. For further details see https://github.com/stevenang/randomness_testsuite.
  
  We will show how we can use this suite to check the randomness of hydrometeorological time series or validate the randomness of hydrometeorological monthly or daily data sets.
  
<span id="1">¹</span> Rozhdenstvenskiy, A. V., & Chevotariov, A. I. (1974). Statistical methods in hydrology (Z. M. Kozhina (ed.)). Guidrometeoizdat..[⏎](#a1)<br>
