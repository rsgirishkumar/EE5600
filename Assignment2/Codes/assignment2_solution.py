import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import seaborn as sns
#event_a=tossing a coin
#event_b = throwing a die
sample_size_a=2#{heads,tails}
sample_size_b=6#{1,2,3,4,5,6}
prob_tails=1/sample_size_a#{1/2}
prob_die_above_4=2/sample_size_b#{2/6=(5,6)}
#p(b/a)=P(ab)/p(a)
#since both are independent events p(ab)=p(a)p(b)=>p(b/a)=p(b)
cond_prob_die_above_4_given_tail=prob_die_above_4
tail_count=0;
#simulating 500 tosses
#for 500 tosses, the sample size may increase to 1/2^500 since each toss is independent, to identify
#how many success and how many failures, binomial distribution may help
#let p be success of toss i.e.tails, q be failure of toss i.e.heads, assuming equally likely outcomes
data_binom=binom.rvs(n=500,p=0.5,size=500)
#n=number of success(individual events),p=probability of success, size=repetition of trails for data points
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(4.5,3)})
ax= sns.distplot(data_binom,
                 kde=False,
                 color="red",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
#count no of tails randomly chosen
tail_events=np.nonzero(data_binom<250)#Checks all trial numbers where tails is outcome,
# since high success rate of tails given as n=500 then most of the trials have tails as outcome
print(tail_events)
#the probability of getting atleast one tail over 500 tosses is total probability(1)-no tails trial
#no tails condition is only one where all outcomes will be heads which is only possibility
#then no of outcomes with atleast a tail
prob_tail_500=(1-(1/pow(2,500)))#approximately 1
#since both events are independent and there exists 499 faavourable outcomes out of 500 for atleast a tail
#the probability of die throwing a number greater than 4 will again be a binomial distribution
#where p=1/3 and q=2/3 and n will be 499 at maximum, its distribution may be seen as below
data_binom2=binom.rvs(n=499,p=1/3,size=499)
sns.set(rc={'figure.figsize':(4.5,3)})
ax= sns.distplot(data_binom2,
                 kde=False,
                 color="blue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
prob_dice_4_499=pow((1/3),499)#since max 499 trials, number greater than 4 can be seen i.e every time you throw a dice number greater than 4 is seen 
print(prob_dice_4_499) 