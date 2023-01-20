class Shape:
	default_mass=1
	default_thita=0
	class equation:
		def init(self,coefficients,value):
			self.coefficients=coefficients
			self.value=value
	def init(self,points=[[0]],masses=[default_mass,default_mass],Thita=default_thita):
		dimension_error=0
		if(not type(points)==list):
			dimension_error=1
		elif(not type(masses)==list):
			dimension_error=2
		elif(not len(points)==len(masses)):
			dimension_error=3
		else:
			for i in points:
				if(not type(i)==list):
					dimension_error=4
					break
				if(len(i)==len(points[0])):
					dimension_error=5
					break
				for j in i:
					if(not(type(j)==float or type(j)==int)):
						dimension_error=6
						break
				if(not dimension_error):
					break
			for i in masses:
				if(not (type(i)==int or type(i)==float)):
					dimension_error=7
					break
				elif(i==0):
					dimension_error=8
					break
		if(dimension_error==1):
			raise "Points has to be a list of points."
		elif(dimension_error==2):
			raise "Masses has to be a list of masses."
		elif(dimension_error==3):
			raise "Number of points must be equal to the number of masses"
		elif(dimension_error==4):
			raise "Each point has to be a list of coordinates."
		elif(dimension_error==5):
			raise "Each point has to have the same dimensions."
		elif(dimension_error==6):
			raise "Each coordinate has to be a number."
		elif(dimension_error==7):
			raise "Each mass has to be a number."
		elif(dimension_error==8):
			raise "Mass of a point cannot be zero."
		else:
			self.points=points#Coordinates of each point
			self.hit_points=points#Coordinates for hitbox
			self.masses=masses#Mass of each point
			self.Thita=Thita#Initial angle of rotation of shape
			self.COM=[0 for i in points[0]]
			self.net_mass=0#Total mass of body
			for i in range(len(points)):
				for j in range(len(points[0])):
					self.COM[j]+=points[i][j]*masses[i]#Adds the jth points mass*(value of coordinate in jth dimension) of ith point
				self.net_mass+=masses[i]#Adds mass of each point
			for i in range(len(COM)):
				self.COM[i]/=self.net_mass#Weighted average of coordinates
	def hitbox_approximate(self):
		def remove_repeats(points):#Remove repeated points to reduce calculation and eliminate zero distance errors
			i=0
			while(i<len(points)):
				j=i+1
				while(j<len(points)):
					if(points[i]==points[j]):
						if(j<len(points)-1):
							points=points[:j]+points[j+1:]
						else:
							points=points[:j]
					j+=1
				i+=1
			return points
		def remove_collinear(points):#Remove collinear points to reduce calculation
			i=0
			while(i<len(points)):
				j=i+1
				while(j<len(points)):
					k=j+1
					while(k<len(points)):
						vect0=[points[k][l]-points[i][l] for l in range(len(points[0]))]
						vect1=[points[j][l]-points[i][l] for l in range(len(points[0]))]
						collinear=True
						for l in range(1,len(vect0)):
							if(not vect0[0]/vect1[1]==vect0[l]/vect1[l]):
								collinear=False
								break
						if(collinear):
							dispij=abs(points[i][0]-points[j][0])
							dispjk=abs(points[j][0]-points[k][0])
							dispki=abs(points[k][0]-points[i][0])
							if(dispij>dispjk and dispij>dispki):
								points.remove(points[k])
								k-=1
							elif(dispjk>dispjk and dispij>dispki):
								points.remove(points[i])
								j=i+1
								k=j
							else:
								points.remove(points[j])
								k=j
						k+=1
					j+=1
				i+=1
			return points
		def find_coefficients(equations):#Required to find equation of the n-1 dimensional body(line,plane...) that contains n points needed for integration
			if(len(equations)==1):#If there is only one equation then the only variable can be calculated
				return [equations[0].value/equations[0].coefficients[0]]
			else:#Using substitution method to solve multiple variables in recursion
				coefficients=[[equations[i].coefficients[j]-equations[0].coefficients[j]*equations[i].coefficients[0]/coefficients[0].equations[0] for j in range(1,len(equations[0].coefficients))] for i in range(1,len(equations))]
				value=[equations[i].value-equations[0].value*equations[i].coefficients[0]/equations[0].coefficients[0] for i in range(1,len(equations))]
				coefficients=find_coefficients([equation(coefficients[i],value[i]) for i in range(len(equations)-1)])
				a0=equations[0].value
				for i in range(1,len(equations[0].coefficients)):
					a0-=coefficients[i]*equations[0].coefficients[i]
				a0/=equations[0].coefficients[0]
				return a0+coefficients
