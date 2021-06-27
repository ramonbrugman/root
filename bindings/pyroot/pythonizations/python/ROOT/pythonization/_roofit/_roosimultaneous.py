# Authors:
# * Jonas Rembser 06/2021
# * Harshal Shende 06/2021

################################################################################
# Copyright (C) 1995-2020, Rene Brun and Fons Rademakers.                      #
# All rights reserved.                                                         #
#                                                                              #
# For the licensing terms see $ROOTSYS/LICENSE.                                #
# For the list of contributors see $ROOTSYS/README/CREDITS.                    #
################################################################################


r"""
/**
\class RooSimultaneous
\brief \parblock \endparblock
\htmlonly
<div class="pyrootbox">
\endhtmlonly

## PyROOT

Some member functions of RooSimultaneous that take a RooCmdArg as argument also support keyword arguments.
So far, this applies to RooSimultaneous::plotOn.
For example, the following code is equivalent in PyROOT:
\code{.py}
# Directly passing a RooCmdArg:
pdfSim.fitTo(data, ROOT.RooFit.Range("r1"))

# With keyword arguments:
pdfSim.fitTo(data, Range="r1")

\endcode

\htmlonly
</div>
\endhtmlonly
*/
"""

from ._utils import _kwargs_to_roocmdargs


class RooSimultaneous(object):
    def plotOn(self, *args, **kwargs):
        # Redefinition of `RooSimultaneous.plotOn` for keyword arguments.
        # The keywords must correspond to the CmdArg of the `plotOn` function.
        args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
        return self._plotOn(*args, **kwargs)
