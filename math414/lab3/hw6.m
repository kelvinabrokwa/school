A = double(rgb2gray(imread('baboon-grayscale.jpg')));
all_s = svds(A, 298);
plot(all_s);
top_s = svds(A, 167);
sum(top_s) / sum(all_s)
top_s = svds(A, 227);
sum(top_s) / sum(all_s)