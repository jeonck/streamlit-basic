import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=25, 
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   label="Carol Danvers",  # 이름 추가
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
nodes.append( Node(id="Iron_Man", 
                   label="Tony Stark",
                   size=25, 
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_ironman.png") 
            )
nodes.append( Node(id="Thor", 
                   label="Thor Odinson",  # 이름 추가
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_thor.png") 
            )

edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 
edges.append( Edge(source="Iron_Man", 
                   label="teammate_of", 
                   target="Spiderman") 
            )
edges.append( Edge(source="Thor", 
                   label="teammate_of", 
                   target="Captain_Marvel") 
            )
edges.append( Edge(source="Iron_Man", 
                   label="mentor_of", 
                   target="Spiderman") 
            )

config = Config(width=900,
                height=900,
                directed=True, 
                physics=True, 
                hierarchical=False,
                nodeSpacing=200,
                layoutAlgorithm={
                    "gravitationalConstant": -50000,
                    "centralGravity": 0.01,
                    "springLength": 200,
                    "springConstant": 0.08,
                    "damping": 0.4,
                    "avoidOverlap": 1
                }
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)