/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ekarpawi <ekarpawi@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/12/15 16:35:53 by ekarpawi          #+#    #+#             */
/*   Updated: 2023/12/15 16:35:53 by ekarpawi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "client.h"

int	main(int argc, char **argv)
{
	if (argc != 3)
	{
		ft_printf("Usage: %s <pid> <message>\n", argv[0]);
		return (1);
	}
	send_message(ft_atoi(argv[1]), argv[2]);
	ft_printf("Message sent!\n");
	return (0);
}
