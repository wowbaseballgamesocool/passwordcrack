local A1, A2 = 727595, 798405  -- 5^17=D20*A1+A2
local D20, D40 = 1048576, 1099511627776  -- 2^20, 2^40
local X1, X2 = 0, 1
function rand()
    local U = X2*A2
    local V = (X1*A2 + X2*A1) % D20
    V = (V*D20 + U) % D40
    X1 = math.floor(V/D20)
    X2 = V - X1*D20
    return V/D40
  end

function Method()
  local runtime = 1
  local attempts = 1
  --for i= 1, 27 do
  while runtime < 27 do

    local x = 1
    password = math.floor(rand() * 100)
    while x ~= password do
      x = x + 1
      attempts = attempts + 1
    end
  runtime = runtime + 1
  end
  print((math.floor(attempts / 27 + 0.5)))
  end



Method()

