import numpy as np 
import MySQLdb
conn = MySQLdb.connect(host = "localhost",port = 8888,db = "restaurant")
x = conn,cursor()
# x.execute("")

# dic = '/Users/rzhan/Desktop/cf/restaurant.json'

# res_num = 50

# a = open(dic,'r')
# rest_info = []
# for i in a:
# 	i = i.strip('{}').split(',')
# 	rest_info.append(i)

# info_refine = []
# info = {}
# rest_id = []
# k = 1
# for i in rest_info:
# 	info.setdefault(k,[])
# 	for j in i:
# 		if 'item_id' in j:
# 			l = j.split(':')
# 			l = l[1].strip('"')
# 			rest_id.append(l)
# 		if 'name' in j:
# 			j = j.split(':')
# 			j = j[1].strip('"')
# 			info[k].append(j)
# 		elif 'rating' in j:
# 			j = j.split(':')
# 			info[k].append(float(j[1]))
# 	k = k+1

# print(info)

# b = open(dic,'r')
# cat = []
# l = 1
# for i in b:
# 	rest_info_2 = []
# 	rest_info_2.append(l)
# 	l = l+1
# 	i = i.split('[')
# 	i = i[1].split(']')
# 	i = i[0].split(',')
# 	for j in range(len(i)):
# 		i[j] = i[j].strip('"')
# 	rest_info_2.append(i)
# 	cat.append(rest_info_2)
# 	rest_info_2 = []

# print(cat)

# all_cat = []
# for i in cat:
# 	for j in i[1]:
# 		if j not in all_cat:
# 			all_cat.append(j)

# col = len(all_cat)
# rating_mat = np.zeros([res_num,col])


# for i in cat:
# 	print(i)
# 	for j in i[1]:
# 		rating_mat[cat.index(i)][all_cat.index(j)] = 1


# def readfile(file_path):
# 	file = open(file_path,'r',encoding = "ISO-8859-1")
# 	info_list = []
# 	for line in file:  
# 		info = line.strip('\n').split('::')
# 		info_list.append(info)
# 	info_array = np.array(info_list)
# 	try:
# 		info_array = info_array.astype(np.int)
# 		return(info_array)
# 	except:
# 		return(info_array)

# ## Euclidean Distace
# ED_correlation_1 = {}
# ED_correlation_ls_1 = []
# ED_correlation = []
# ED_correlation_ls = []

# for i in range(len(rating_mat)):
#     for j in range(len(rating_mat)):
#         ED = np.linalg.norm(rating_mat[i]-rating_mat[j])
#         k = j+1
#         if ED not in ED_correlation_1:
#         	ED_correlation_1.setdefault(ED,[k])
#         else:
#         	ED_correlation_1[ED].append(k)
#         if ED not in ED_correlation_ls_1:
#         	ED_correlation_ls_1.append(ED)
#     ED_correlation.append(ED_correlation_1)
#     ED_correlation_1 = {}
#     ED_correlation_ls.append(ED_correlation_ls_1)
#     ED_correlation_ls_1 = []

# # conn = MySQLdb.connect(host = "localhost",
# # 						user = 'root',
# # 						passwd = "root",
# # 						db = "")
# # x = conn,cursor()
# # x.execute("")

# while 1:
# 	res_id = input()
# 	# x.execute("")
# 	res_id = res_id.split(' ')
# 	re_rec_ = []
# 	recommendation = []
# 	for s in res_id:
# 		i = int(s)-1
# 		for j in ED_correlation[int(i)]:
# 			for k in ED_correlation[int(i)][j]:
# 				re_rec = [k,j,1/info[k][1]]
# 				re_rec_.append(re_rec)
# 				re_rec = []
# 	re_rec_ = sorted(re_rec_, key = lambda x:(x[1],x[2]))
# 	for i in re_rec_:
# 		if i[0] not in recommendation:
# 			recommendation.append(i[0])
# 	for i in res_id:
# 		recommendation.remove(int(i))
# 	rec_lst = []
# 	# print(recommendation)
# 	for i in recommendation:
# 		rec_lst.append(info[i][0])
# 		# rec_lst.append(rest_id[i-1])
# 	try:
# 		# print(rec_lst[1:20])
# 		print(recommendation[0:19])
# 	except Exception:
# 		print(rec_lst)





# while 1:
# 	movie_ID = input()
# 	try:
# 		relative_list = sorted(ED_correlation_ls[int(movie_ID)-1])
# 		recommendation = []
# 		for i in relative_list:
# 			same_level = ED_correlation[int(movie_ID)-1][i]
# 			rating = []
# 			for j in same_level:
# 				rating.append(info[j][1])
# 			re_rec_ = np.array([same_level,rating])
# 			re_rec_ = re_rec_.T
# 			re_rec_ = re_rec_[re_rec_[:,1].argsort()]
# 			re_rec_ = re_rec_[::-1]
# 			recommendation.append(re_rec_[:,0])
# 		rec_lst = []
# 		for i in recommendation:
# 			for j in i:
# 				rec_lst.append(info[j][0])
# 	except IndexError:
# 		print("The restaurant is not in the list")

# # Pearson correlation coefficient
# for i in range(len(rating_mat)):
#     for j in range(len(rating_mat)):
#         mean_i = np.mean(rating_mat[i])
#         mean_j = np.mean(rating_mat[j])
#         rho = np.dot((rating_mat[i]-mean_i),(rating_mat[j]-mean_j))
#         print(rho)





                
                