function[EncryptString] = caeser(EncryptString, Shift)
    EncryptString = upper(EncryptString);
    for n = 1:1:numel(EncryptString)-1
        if isletter(EncryptString(n)) == 0
            EncryptString(n) = [];
        else
            EncryptString(n) = EncryptString(n) + Shift;
        end
    end
    char(EncryptString);
end

            