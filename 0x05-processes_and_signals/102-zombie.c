#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - implement an infinite while loop
 * Return: 0
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
 * main - program start point
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i;

	i = 0;
	while (i < 5)
	{
		pid = fork();
		if (pid != 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);

		i++;
	}

	infinite_while();
	return (0);

}
