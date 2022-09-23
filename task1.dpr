Program training1;


Var
peopleN, cakesN: Integer;
k1, k2, k3: Real;
n2, n3: Real;
n1: Integer;
askMN: boolean = true;
askUser: boolean = true;
wroteAnswer: boolean = false;



Begin
while (askUser) do
begin
  try
    if (askMN) then
    begin
      write('Enter monarch amount and cakesN(using space as delimiter): '); 
      read(peopleN, cakesN);
    end;
    if (peopleN < 0) or (cakesN < 0) then
    begin
      writeln('Please enter positive numbers')
    end
    else
    begin
      write('Enter how many cakes does each monarch eat(using space as delimiter): ');
      read(k1, k2, k3);
      askUser := false;
      if k2 = k3 then
      begin
        writeln('k2 cannot be equal to k3'); 
        askMN := false;
        askUser := true;
      end;
      if (k1 < 0) or (k2 < 0) or (k3 < 0) then
      begin
        writeln('k1, k2, k3 must be greater than zero'); 
        askMN := false;
        askUser := true;
      End
    end; 
  except
    writeln('Invalid input');
  end;
end;
  for n1 := 0 to round(cakesN / k1) do 
  begin
    if (k3 - k2 <> 0) then
    begin
      n3 := (cakesN + n1 * (k2 - k1) - peopleN * k2) / (k3 - k2);
      n2 := peopleN - n1 - n3;
      if (n2-round(n2)=0) and (n3-round(n3)=0) and (n2 >= 0) and (n3 >= 0) then
      begin
        writeln(n1, '  ', n2:2:0, '  ',n3:2:0);
        wroteAnswer := true;
      end;
    end;
  end;
  if (not wroteAnswer) then
    writeln('There is no way... to feed everyone');
End.