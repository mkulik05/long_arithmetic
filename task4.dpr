program training4;

{$APPTYPE CONSOLE}

uses
    Math;

type
    CharArray = array of char;

Var
    n1, n2, result: AnsiString;
    n1_arr, n2_arr: array of char;
// return -1 if n1 < n2, 0 if n1 = n2, 1 if n1 > n2
function Compare(n1, n2: AnsiString): Integer;
var
    l1, l2, i, n1_digit, n2_digit, trash: Integer;
begin
    l1 := length(n1);
    l2 := length(n2);
    if l1 < l2 then
        Result := -1;
    if l1 > l2 then
        Result := 1;
    if l1 = l2 then
    begin
        Result := 0;
        for i := 1 to l1 do
        begin
            Val(n1[i], n1_digit, trash);
            Val(n2[i], n2_digit, trash);
            if (n1_digit > n2_digit) then
            begin
                Result := 1;
                break;
            end;
            if (n1_digit < n2_digit) then
            begin
                Result := -1;
                break;
            end;
        end;

    end;
end;


function Sum(n1, n2: AnsiString): AnsiString;
var
    i, n1_digit, n2_digit, l1, l2, trash, l_delta: Integer;
    save_one: Integer;
    sum: Integer;
    answ, res_string, n0, second_part: AnsiString;
begin
    save_one := 0;
    if (length(n1) > length(n2)) then
    begin
        n0 := n1;
        n1 := n2;
        n2 := n0;
    end;
    l1 := length(n1);
    l2 := length(n2);
    l_delta := l2 - l1;
    for i := l1 downto 1 do
    begin
        Val(n1[i], n1_digit, trash);
        Val(n2[i + l_delta], n2_digit, trash);
        sum := n1_digit + n2_digit;

        sum := sum + save_one;
        if sum > 9 then
        begin
            save_one := 1;
            sum := sum - 10;
        end
        else
        begin
            save_one := 0;
        end;

        Str(sum, res_string);
        answ := res_string + answ;
    end;

    i := l_delta;
    second_part := n2;
    setLength(second_part, i);

    while (save_one = 1) do
    begin

        Val(n2[i], n2_digit, trash);
        if n2_digit < 9 then
        begin
            Str(n2_digit + 1, res_string);
            second_part[i] := res_string[1];
            break
        end
        else
        begin
            second_part[i] := '0';
        end;
        if i = 1 then
        begin
            second_part := '1' + second_part;
            break;
        end;
        i := i - 1;
    end;
    Result := second_part + answ;

end;



function Subtract(n1, n2: AnsiString): AnsiString;
var
    i, n1_digit, n2_digit, l1, l2, trash, l_delta: Integer;
    save_one: Integer;
    Subtraction: Integer;
    answ, res_string, n0, second_part: AnsiString;
begin
    save_one := 0;
    if (length(n1) < length(n2)) then
    begin
        n0 := n1;
        n1 := n2;
        n2 := n0;
    end;

    l1 := length(n1);
    l2 := length(n2);
    l_delta := l1 - l2;
    writeln(l1, ' ', l2);
    for i := l2 downto 1 do
    begin
        Val(n1[i + l_delta], n1_digit, trash);
        Val(n2[i], n2_digit, trash);
        Subtraction := n1_digit - n2_digit;

        Subtraction := Subtraction + save_one;
        if Subtraction < 0 then
        begin
            save_one := -1;
            Subtraction := Subtraction + 10;
        end
        else
        begin
            save_one := 0;
        end;

        Str(Subtraction, res_string);
        answ := res_string + answ;
    end;

    i := l_delta;
    second_part := n2;
    setLength(second_part, i);

    while (save_one = -1) do
    begin

        Val(n2[i], n2_digit, trash);
        if n2_digit > 0 then
        begin
            Str(n2_digit - 1, res_string);
            second_part[i] := res_string[1];
            break
        end
        else
        begin
            second_part[i] := '9';
        end;
        i := i - 1;
    end;
    Result := second_part + answ;

end;


function Multiplication1(n1, n2: AnsiString): AnsiString;
var
    i, n1_digit, n2_digit, res, l1, l2, trash: Integer;
    add_to_next: Integer;
    last_digit: AnsiString;
    multipl: Integer;
    answ, res_string: AnsiString;
begin
    add_to_next := 0;
    Val(n2, n2_digit, trash);
    l1 := length(n1);
    for i := l1 downto 1 do
    begin
        Val(n1[i], n1_digit, trash);
        multipl := n1_digit * n2_digit;

        multipl := multipl + add_to_next;
        if multipl > 9 then
        begin
            add_to_next := multipl DIV 10;
            multipl := multipl MOD 10;
        end
        else
        begin
            add_to_next := 0;
        end;

        Str(multipl, res_string);
        answ := res_string + answ;
    end;
    if (add_to_next > 0) then
        Str(add_to_next, last_digit);
        answ := last_digit + answ;
    Result := answ;
end;



function Multiplication2(n1, n2: AnsiString): AnsiString;
var
    i, n1_digit, n2_digit, l1, l2, a: Integer;
    answ, res_string, res, multipl: AnsiString;
    ops: array of AnsiString;
begin
    l1 := length(n1);
    l2 := length(n2);
    setLength(ops, l2);
    for i := l2 downto 1 do
    begin
        res :=  Multiplication1(n1, n2[i]);
        if l2 - i  > 0 then
        begin
          for a := 1 to (l2 - i) do
          begin
            res := res + '0';
          end;
        end;
        ops[i] := res;
    end;
    for i := 1 to l2 do
        multipl := Sum(multipl, ops[i]);

    Result := multipl;
end;


function StrToArray(str: string): CharArray;
var
    len, i: Integer;
    res: CharArray;
begin
len := length(str);
    setLength(Result, len);
    for i := 1 to len  do
    begin
        Result[i] := str[i];
    end;
end;

Begin
    readln(n1);
    readln(n2);
    // n1_arr := StrToArray(n1);
    // n2_arr := StrToArray(n2);
    Writeln(Sum(n1, n2));
End.