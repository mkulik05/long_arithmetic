program training4;

{$APPTYPE CONSOLE}

uses
    Math;

type
    IntegerArray = array of Integer;

Var
    n1, n2, result: AnsiString;
    n1_arr, n2_arr: IntegerArray;


function ShowArray(arr: IntegerArray): String;
var 
    i: Integer;
begin
    for i := 0 to length(arr) - 1 do
        write(arr[i]);
    writeln('');
end;

function ReverseArray(arr: IntegerArray): IntegerArray;
var
    i, len, len2, tmp: Integer;

begin
    Result := arr;
    len := length(arr) - 1;
    len2 := len DIV 2;
    for i := 0 to len2 do
    begin
        tmp := Result[i];
        Result[i] := Result[len - i];
        Result[len - i] := tmp;
    end;
end;


// return -1 if n1 < n2, 0 if n1 = n2, 1 if n1 > n2
function Compare(n1, n2: IntegerArray): Integer;
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
        for i := 0 to l1 - 1 do
        begin
            n1_digit := n1[i];
            n2_digit := n2[i];
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

function Sum(n1, n2: IntegerArray): IntegerArray;
var
    i, n1_digit, n2_digit, l1, l2, l_delta: Integer;
    save_one: Integer;
    sum: Integer;
    answ, n0: IntegerArray;
begin
    save_one := 0;
    l1 := length(n1);
    l2 := length(n2);
    if (l1 > l2) then
    begin
        n0 := n1;
        n1 := n2;
        n2 := n0;
    end;
    l1 := length(n1);
    l2 := length(n2);
    answ := n2;
    l_delta := l2 - l1;
    for i := 0 to l1 - 1 do
    begin
        n1_digit := n1[i];
        n2_digit := n2[i];
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

        answ[i] := sum;
    end;

    i := l1;
    while (save_one = 1) do
    begin
        if i >= l2 then
        begin
            setLength(answ, l2 + 1);
            answ[l2] := 1;
            break;
        end;

        n2_digit := n2[i];
        writeln(n2_digit);
        if n2_digit = 9 then
        begin

            answ[i] := 0;
        end
        else
        begin
            answ[i] := n2_digit + 1;
            break
        end;
        i := i + 1;
    end;
    Result := answ;

end;



function Subtract(n1, n2: IntegerArray): IntegerArray;
var
    i, n1_digit, n2_digit, l1, l2, l_delta: Integer;
    save_one: Integer;
    substraction: Integer;
    answ, n0: IntegerArray;
begin
    save_one := 0;
    l2 := length(n2);
    answ := n1;
    for i := 0 to l2 - 1 do
    begin
        n1_digit := n1[i];
        n2_digit := n2[i];
        substraction := n1_digit - n2_digit;

        substraction := substraction + save_one;
        if substraction < 0 then
        begin
            save_one := -1;
            substraction := substraction + 10;
        end
        else
        begin
            save_one := 0;
        end;

        answ[i] := substraction;
    end;

    i := l2;
    while (save_one = -1) do
    begin
        n1_digit := n1[i];
        if n1_digit = 0 then
        begin
            answ[i] := 9;
        end
        else
        begin
            answ[i] := n1_digit - 1;
            break
        end;
        i := i + 1;
    end;
    Result := answ;

end;


function Multiplication1(n1: IntegerArray; n2: Integer): IntegerArray;
var
    i, res, l1: Integer;
    add_to_next: Integer;
    multipl: Integer;
    answ, res_string: IntegerArray;
begin
    add_to_next := 0;

    l1 := length(n1);
    answ := n1;
    for i := 0 to l1 - 1 do
    begin
        multipl := n1[i] * n2;

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

        answ[i] := multipl;
    end;
    if (add_to_next > 0) then
        setLength(answ, l1 + 1);
        answ[l1] := add_to_next;
    Result := answ;
end;



// function Multiplication2(n1, n2: AnsiString): AnsiString;
// var
//     i, n1_digit, n2_digit, l1, l2, a: Integer;
//     answ, res_string, res, multipl: AnsiString;
//     ops: array of AnsiString;
// begin
//     l1 := length(n1);
//     l2 := length(n2);
//     setLength(ops, l2);
//     for i := l2 downto 1 do
//     begin
//         res :=  Multiplication1(n1, n2[i]);
//         if l2 - i  > 0 then
//         begin
//           for a := 1 to (l2 - i) do
//           begin
//             res := res + '0';
//           end;
//         end;
//         ops[i] := res;
//     end;
//     for i := 1 to l2 do
//         multipl := Sum(multipl, ops[i]);

//     Result := multipl;
// end;


function StrToArray(str: string): IntegerArray;
var
    len, i, digit: Integer;
    res: IntegerArray;
begin
    len := length(str);
    setLength(Result, len);
    for i := 1 to len do
    begin
        Val(str[i], digit);
        Result[i - 1] := digit;
    end;
end;

Begin
    readln(n1);
    readln(n2);
    n1_arr := ReverseArray(StrToArray(n1));
    n2_arr := ReverseArray(StrToArray(n2));


    ShowArray(ReverseArray(Multiplication1(n1_arr, 9)));
End.