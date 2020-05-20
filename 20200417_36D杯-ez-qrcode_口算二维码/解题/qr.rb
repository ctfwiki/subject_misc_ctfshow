data = '0100000101100110011001101100011000010110011101111011010101000110011101000011011000010110111001101110011011110111010001000111011001010111010001001000011011110111010101110011011001010111110100001110110000010001'
alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'.chars

def read(str, size)
  str.slice!(0, size)
end

def kanji(num)
  if num >= 0x1740
    (0xC140 + num / 0xC0 * 0x100 + num % 0xC0)
      .chr(Encoding::Shift_JIS).encode(Encoding::UTF_8)
  else
    (0x8140 + num / 0xC0 * 0x100 + num % 0xC0)
      .chr(Encoding::Shift_JIS).encode(Encoding::UTF_8)
  end
end

loop do
  case mode = read(data, 4)
  when '0010' # Alphanumeric
    count = read(data, 9).to_i(2)
    (count / 2).times do
      chunk = read(data, 11).to_i(2)
      print alphanumeric[chunk / 45] + alphanumeric[chunk % 45]
    end
    print alphanumeric[read(data, 11).to_i(2)] if count.odd?
  when '0100' # Byte
    count = read(data, 8).to_i(2)
    count.times do
      print read(data, 8).to_i(2).chr
    end
  when '1000' # Kanji
    count = read(data, 8).to_i(2)
    count.times do
      print kanji(read(data, 13).to_i(2))
    end
  when '0000' # Terminate
    break
  else
    fail "Unhandled mode #{mode}"
  end
end
