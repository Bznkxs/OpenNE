from .graph import Dataset, Graph, LocalFile, Adapter, NetResources, create_self_defined_dataset
from .matlab_matrix import MatlabMatrix, PPI, Wikipedia, Flickr, BlogCatalog
from .wiki import Wiki
from .planetoid_dataset import PubMed, Cora, CiteSeer
from .graphs import Graphs, MUTAG, PTC_MR, IMDB_BINARY, IMDB_MULTI, REDDIT_BINARY

datasetlist = [PPI, Wikipedia, Flickr, BlogCatalog, Wiki, PubMed, Cora, CiteSeer, MUTAG, PTC_MR, IMDB_BINARY, IMDB_MULTI, REDDIT_BINARY]
datasetdict = {Cls.__name__.lower(): Cls for Cls in datasetlist}

