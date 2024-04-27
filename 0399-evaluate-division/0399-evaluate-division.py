class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        def getTotal(source, dest, current=1):
            seen.add(source)
            result = -1
            neibours = graph[source]
            if dest in neibours:
                result = current * neibours[dest]
            else:
                for next , value in neibours.items():
                    if next not in seen:
                        result = getTotal(next,dest, current * value)
                        if result != -1:
                            break
            seen.remove(source)
            return result

        result = []
        for source , dest in queries:
            if source not in graph or dest not in graph:
                result.append(-1)
            elif source == dest:
                result.append(1)
            else:
                seen = set()
                result.append(getTotal(source,dest))
        return result