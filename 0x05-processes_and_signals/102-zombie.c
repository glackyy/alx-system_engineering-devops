#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
/**
 * infinite_while - Entry Function
 * Return: 0 (SUCCESS)
 */
int infinite_while(void)
{
	while (1)
    	{
        	sleep(1);
    	}
    	return (0);
}

/**
 * main - Entry Point
 * Return: 0 (SUCCESS)
 */
int main(void)
{
	pid_t p;
	char ct;
	ct = 0;
	while (ct < 5)
	{
		p = fork();
		if (p > 0)
		{
			printf("Zombie process created, PID %d\n", p);
			sleep(1);
			ct++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
