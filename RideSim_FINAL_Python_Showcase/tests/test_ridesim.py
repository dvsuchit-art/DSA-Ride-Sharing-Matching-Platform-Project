import unittest
from ridesim.models import Driver,Rider
from ridesim.cost import build_cost_matrix
from ridesim.greedy import greedy_match
from ridesim.hungarian import hungarian_match
from ridesim.engine import scenario,compare_solvers
class T(unittest.TestCase):
 def test_distance(self): self.assertEqual(build_cost_matrix([Driver("D",0,0)],[Rider("R",3,4)])[0][0],5)
 def test_unique_assignment(self):
  d,r=scenario(8,123); m=hungarian_match(d,r); self.assertEqual(len({x.rider_index for x in m}),8)
 def test_optimal_no_worse(self):
  d,r=scenario(10,9); x=compare_solvers(d,r); self.assertLessEqual(x["optimal"]["total_distance"],x["greedy"]["total_distance"]+1e-9)
if __name__=="__main__": unittest.main()
