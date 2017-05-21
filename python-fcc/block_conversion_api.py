from .generic_api import *

# Simple Python wrapper around the Block Conversion API provided by the FCC.

class BlockConversionAPI(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, [("get_block", "http://data.fcc.gov/api/block/find")])


# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = BlockConversionAPI()
  print(bc.get_block(lat=41, int=-87)) # (Should be San Francisco)