type 'a arbre = 
  | Vide
  | Noeud of 'a* 'a arbre* 'a arbre 
;;


let rec remplir s op = match (s,op) with 
  |([] , _) -> Vide
  |(_ , []) -> Vide 
  |([x] , [y]) -> 
      if y <= x then 
        Noeud (x ,Noeud(x-y, Vide , Vide) ,Noeud(x , Vide , Vide)) 
      else 
        Noeud (x , Vide ,Noeud(x,Vide,Vide))  
  |(t::q , [y]) -> 
      if y <= t then 
        Noeud (t , Noeud(t-y, Vide , Vide) , Noeud(t, Vide , Vide)) 
      else 
        Noeud (t , Vide , remplir q op) 
  |([x], t::q) -> 
      if t <= x then
        Noeud (t , remplir [x-t] q , remplir s q)
      else 
        Noeud (t , Vide , remplir [x] q ) 
  |(t1::q1 , t2::q2) -> 
      if t2 <= t1 then 
        Noeud (t1 , remplir ([t2-t1]@q1) q2 , remplir s q2 ) 
      else
        Noeud (t1 , Vide , remplir s q2) 
;; 

let s = [2;3;4] ;;
let op = [3;1;1];;

remplir s op ;;

