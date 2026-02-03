function [letter, maxlen] = inarow(str)
    letter = '';
    currletter = '';
    maxlen = 0;
    currlen = 1;
    for i = 1:length(str)
        if str(i) == currletter
            currlen = currlen + 1;
        else
            if maxlen < currlen
                maxlen = currlen;
                letter = currletter;
            end
            currletter = str(i);
            currlen = 1;
        end
    end
end