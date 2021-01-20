from .gf import GraphFactorization
from .grarep import GraRep
from .hope import HOPE
from .lap import LaplacianEigenmaps
from .line import LINE
from .lle import LLE
from .node2vec import Node2vec, DeepWalk
from .sdne import SDNE
from .tadw import TADW
from .gcn.gcnAPI import GCN
from .models import ModelWithEmbeddings
from .gae import GAE
from .vgae import VGAE
from .ss_gae import SS_GAE
from .ss_deepwalk import SS_DeepWalk
from .ss_nodemodel import SS_NodeModel
# add import of new models here

modellist = [GraphFactorization, GraRep, HOPE, LaplacianEigenmaps, LINE,
             LLE, Node2vec, DeepWalk, SDNE, TADW, GCN, GAE, VGAE, SS_GAE,
             SS_DeepWalk, SS_NodeModel]  # add new models here
modeldict = {Cls.__name__.lower(): Cls for Cls in modellist}
modeldict.update({Cls.othername.lower(): Cls for Cls in modellist if 'othername' in Cls.__dict__})
