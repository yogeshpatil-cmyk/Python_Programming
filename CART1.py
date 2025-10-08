# in jupyter notebook
import sklearn
import matplotlib
import pydot
import seaborn as sns
import six

from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier

df = sns.load_dataset('titanic')

dep_var = 'survived'
id_var = ['pclass', 'sex']
indep_var = ['age', 'sibsp', 'parch', 'fare']

# tree
tree = DecisionTreeClassifier(max_depth=2)
tree.fit(df[indep_var].fillna(-9999), df[dep_var]) 

features = [u'{}'.format(c) for c in indep_var]
# viz
dot_data = StringIO()  
export_graphviz(tree, out_file=dot_data,  
                    feature_names=features,
#                     class_names=tree.classes_,  
#                     filled=True, rounded=True,  
                    special_characters=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0]  
Image(graph.create_png()) 
