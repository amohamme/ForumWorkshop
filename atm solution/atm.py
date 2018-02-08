########################################
# ATM 
########################################

# Allowed papers: 100, 50, 10, 5, and rest of request

def atm(money,request,allowed_papers):

	print '==========================================='
	print ' ATM Requested Amount : ', request
	print ' ATM Allowed papers   : ', allowed_papers[0],',',allowed_papers[1],',',allowed_papers[2],',',allowed_papers[3],',',' change < ' ,allowed_papers[3] 
	print '==========================================='
	
	# Check Requested Amount - Enough Balance
	if (request > money):
		print 'ATM maximum transaction is', money ,'please use less amount'
		return
		
	# Check Requested Amount - Negative Request
	if (request <= 0):
		print 'Wrong negative requested amount, please enter a postive amount'
		return

	reminder = 0
	
	while request > 0:
		if (request >= allowed_papers[0]):
			print 'give',allowed_papers[0]
			request = request - allowed_papers[0]
		elif (request >= allowed_papers[1]):
			print 'give', allowed_papers[1]
			request = request - allowed_papers[1]
		elif (request >= allowed_papers[2]):
			print 'give', allowed_papers[2]
			request = request - allowed_papers[2]
		elif (request >= allowed_papers[3]):
			print 'give', allowed_papers[3]
			request = request - allowed_papers[3]
		else:
			print 'give',request
			return


allowed_papers = [100,50,10,5]

300, 800, 150, 5, -20, 0

atm(500,277,allowed_papers)
print ' '
atm(500,300,allowed_papers)
print ' '
atm(500,800,allowed_papers)
print ' '
atm(500,150,allowed_papers)
print ' '
atm(500,5,allowed_papers)
print ' '
atm(500,-20,allowed_papers)
print ' '
atm(500,0,allowed_papers)
print ' '
atm(500,500,allowed_papers)
print ' '
atm(500,11,allowed_papers)