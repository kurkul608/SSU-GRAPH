



int dfs(int u, int Cmin):         // Cmin — пропускная способность в текущем подпотоке
   if u = t
       return Cmin
   visited[u] = true
   for v in u.children
       auto uv = edge(u, v)
       if not visited[v] and uv.f < uv.c
           int delta = dfs(v, min(Cmin, uv.c - uv.f))
           if delta > 0
               uv.f += delta
               uv.backEdge.f -= delta
               return delta
   return 0