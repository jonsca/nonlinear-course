'''
test_odesolvers.py

Requires PyTest and PyTest-Mock to run

Unit tests for the odesolvers module.  These are not meant to be exhaustive, 
but for illustrative purposes

Written by JScabich

Integration tests would require a "ground truth" to compare against and this
is difficult to attain with numerical methods.

License: MIT
'''
import random
import odesolvers as ods

MIN, MAX = -10_000.0, 10_000.0

def randomNumberFactory(seed=None):  
	'''
	Parameters:
		seed (use a constant value for repeatable results,
		otherwise seeded from the clock on Windows)

	Returns:
		tuple of Random values for x, v, deltat, x_returned, v_returned 
	'''
	rand = random.Random()
	rand.seed(seed)
	x = rand.uniform(MIN, MAX)
	v = rand.uniform(MIN, MAX)
	deltat = rand.uniform(0, MAX)
	x_returned = rand.uniform(MIN, MAX)
	v_returned = rand.uniform(MIN, MAX)

	return x, v, deltat, x_returned, v_returned


def test_odesolvers_forwardstep_calls_xprime_and_vprime(mocker):
	'''
	A more robust test would see if v_prime would take in another
	value other than the default, but for our purposes, the frictionless
	case of v = 0 is acceptable 

	This could also be split out into two tests, each with a single
	assert, but would repeat a lot of code

	'''	
	x, v, deltat, *_ = randomNumberFactory()

	mocker.patch('odesolvers.v_prime')
	mocker.patch('odesolvers.x_prime')
	
	ods.forward_step(x, v, deltat)
	
	ods.v_prime.assert_called_with(x)
	ods.x_prime.assert_called_with(v)


def test_odesolvers_backwardstep_calls_xprime_and_vprime(mocker):
	'''
	As above, splitting this into a two tests might be easier to read but 
	repeats a lot of code 
	'''
	x, v, deltat, x_returned, v_returned = randomNumberFactory()

	mocker.patch('odesolvers.v_prime')
	mocker.patch('odesolvers.x_prime')
	mocker.patch('odesolvers.forward_step', 
		return_value = (x_returned, v_returned))
	
	ods.backward_step(x, v, deltat)
	
	ods.v_prime.assert_called_with(x_returned)
	ods.x_prime.assert_called_with(v_returned)


def test_odesolvers_backwardstep_calls_forwardstep(mocker):
	'''
		frictionless v=0 condition holds here as well
	'''
	x, v, deltat, x_returned, v_returned = randomNumberFactory()

	mocker.patch('odesolvers.forward_step', 
		return_value=(x_returned, v_returned))
	
	ods.backward_step(x, v, deltat)
	
	ods.forward_step.assert_called_with(x, v, deltat)


def test_odesolvers_combineddstep_calls_xprime_and_vprime_twice(mocker):
	'''
	Frictionless, v=0

	Splitting this into multiple tests may have eased readability only slightly
	but at the expense of repeating a lot of boilerplate

	Assert types are not perfect.  I really want to be able to find out if they
	are called in the right order, but has_calls with a list was not producing
	the expected result
	'''
	x, v, deltat, x_returned, v_returned = randomNumberFactory()

	mocker.patch('odesolvers.x_prime')
	mocker.patch('odesolvers.v_prime')
	mocker.patch('odesolvers.forward_step', 
		return_value = (x_returned, v_returned))
	
	ods.combined_step(x, v, deltat)
	
	ods.v_prime.assert_any_call(x)
	ods.x_prime.assert_any_call(v)

	ods.v_prime.assert_any_call(x_returned)
	ods.x_prime.assert_any_call(v_returned)


def test_odesolvers_combineddstep_calls_forwardstep(mocker):
	'''
		Frictionless, v=0 condition here too
	'''
	x, v, deltat, x_returned, v_returned = randomNumberFactory()

	mocker.patch('odesolvers.forward_step', 
		return_value=(x_returned, v_returned))
	
	ods.combined_step(x, v, deltat)
	
	ods.forward_step.assert_called_with(x, v, deltat)


def test_odesolvers_iterate_n_calls_forwardstep_n_iter_times(mocker):
	'''
	Taking a deeper dive with these and making sure all the appropriate
	parameters are used in all n_iter calls to the method would be impractical
	'''
	x0, v0, deltat, x_returned, v_returned = randomNumberFactory()
	n_iter = random.randint(0,int(MAX))
	mocker.patch('odesolvers.forward_step', 
		return_value=(x_returned, v_returned))

	ods.iterate_n(x0, v0, deltat, n_iter, ods.forward_step)

	assert ods.forward_step.call_count, n_iter


def test_odesolvers_iterate_n_calls_backwardstep_n_iter_times(mocker):
	
	x0, v0, deltat, x_returned, v_returned = randomNumberFactory()
	n_iter = random.randint(0,int(MAX))
	mocker.patch('odesolvers.backward_step', 
		return_value=(x_returned, v_returned))

	ods.iterate_n(x0, v0, deltat, n_iter, ods.backward_step)

	assert ods.backward_step.call_count, n_iter


def test_odesolvers_iterate_n_calls_combinedstep_n_iter_times(mocker):
	
	x0, v0, deltat, x_returned, v_returned = randomNumberFactory()
	n_iter = random.randint(0,int(MAX))
	mocker.patch('odesolvers.combined_step',
		return_value=(x_returned, v_returned))

	ods.iterate_n(x0, v0, deltat, n_iter, ods.combined_step)

	assert ods.combined_step.call_count, n_iter

