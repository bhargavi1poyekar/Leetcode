class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        recipes_to_idx = {recipe:idx for idx, recipe in enumerate(recipes)}

        graph = defaultdict(list)
        indegree = [0] * len(recipes)

        for idx, ingredient in enumerate(ingredients):
            for ing in ingredient:
                if ing not in supplies:
                    graph[ing].append(recipes[idx])
                    indegree[idx] += 1
            
        queue = deque()
        # Add recipes with 0 indegree, no dependency (all available supplies) in queue
        for idx, count in enumerate(indegree):
            if count == 0:
                queue.append(idx)
        
        possible_recipes = []
        
        while queue:
            idx = queue.popleft()
            recipe = recipes[idx]
            possible_recipes.append(recipe)

            for nghbr in graph[recipe]:
                indegree[recipes_to_idx[nghbr]] -= 1
                if indegree[recipes_to_idx[nghbr]] == 0:
                    queue.append(recipes_to_idx[nghbr])
        
        return possible_recipes
            
